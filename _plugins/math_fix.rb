Jekyll::Hooks.register(:documents, :pre_render) do |doc|
  doc.content.gsub!(/(?<!\\)\$(?!\$)/, '$$')
end
